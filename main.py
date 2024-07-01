from clouds.aws.aws_aux_func import get_subnet_id, get_vpc_id, get_vm_id, get_ip_id, get_dns_zone_id, select_ami, list_vm_names
from clouds.aws.vpc.aws_vpc_func import create_vpc, delete_vpc, list_vpcs
from clouds.aws.vpc.aws_subnet_func import create_subnet, delete_subnet
from clouds.aws.vm.aws_vm_func import create_vm, delete_vm, start_vm, stop_vm, list_vms
from clouds.aws.vm.aws_create_ssh_keys import create_key_pair, list_key_pairs
from clouds.aws.vm.aws_ip_func import create_ip, list_ips, attach_public_ip, detach_public_ip, delete_ip
from clouds.aws.bucket.aws_bucket_func import create_bucket, delete_bucket, configure_web_bucket, list_buckets, upload_file_to_bucket, download_file_from_bucket
from clouds.aws.dns.aws_dns_func import create_dns_zone, list_dns_zones, create_dns_record, list_dns_records, delete_dns_record, delete_dns_zone

from clouds.azure.azure_resources_group_func import azure_list_resource_groups, azure_list_resources_from_group
from clouds.azure.azure_vpc_func import azure_create_vpc, azure_delete_vpc, azure_list_vpcs
from clouds.azure.azure_vm_func import azure_create_vm, azure_delete_vm, azure_start_vm, azure_stop_vm
from clouds.azure.azure_ip_func import azure_create_ip, azure_delete_ip, azure_attach_ip


def menu_main():
    while True:
        print("Selecciona el proveedor cloud que deseas utilizar:")
        print("1. Amazon Web Services")
        print("2. Microsoft Azure")
        print("Q|q. Salir")
        op1 = input("Opcion >>> ")
        print()

        if op1 == "1":
            menu_aws()
        elif op1 == "2":
            menu_azure()
        elif op1 in ["Q", "q"]:
            break
        else:
            print("Opcion no valida")
            print()

def menu_aws():
    # FIXME: Al listar los recursos aparecen None que no se que son
    print("Recursos activos actualmente:")
    print()
    print("Redes virtuales (VPC):")
    print(list_vpcs())
    print()
    print("Maquina Virtuales (EC2):")
    print(list_vms())
    print()
    print("Buckets almacenamiento (S3):")
    print(list_buckets())
    print()
    print("Zonas DNS:")
    print(list_dns_zones())
    print()
    print()

    while True:
        print("Selecciona el servicio de Amazon Web Services que deseas utilizar:")
        print("1. Redes virtuales (VPC)")
        print("2. Maquinas Virtuales (EC2)")
        print("3. Buckets almacenamiento (S3)")
        print("4. DNS (Route 53)")
        print("Q|q. Volver")
        option = input("Opcion >>> ")
        print()

        if option == "1":
            menu_aws_vpc()
            print()

        elif option == "2":
            menu_aws_vm()
            print()

        elif option == "3":
            menu_aws_bucket()
            print()

        elif option == "4":
            menu_aws_dns()
            print()
        
        elif option in ["Q", "q"]:
            break

        else:
            print("Opcion no valida")
            print()



def menu_azure():
    print("Grupos de recursos activos:")
    print()
    print(azure_list_resource_groups())
    print()
    print()

    while True:
        print("Selecciona el servicio de Azure que deseas utilizar:")
        print("1. Listar grupo de recursos")
        print("2. Redes virtuales")
        print("3. Maquinas Virtuales")
        print("Q|q. Volver")
        option = input("Opcion >>> ")
        print()

        if option == "1":
            group = input("Nombre del grupo de recursos: ")
            azure_list_resources_from_group(group)

        elif option == "2":
            menu_azure_vpc()
            print()

        elif option == "3":
            menu_azure_vm()
            print()
        
        elif option in ["Q", "q"]:
            break

        else:
            print("Opcion no valida")
            print()



def menu_aws_vpc():
    while True:
        print("Selecciona la operacion que deseas realizar:")
        print("1. Crear VPC")
        print("2. Listar VPCs")
        print("3. Eliminar VPC")
        print("Q|q. Salir")
        option = input("Opcion >>> ")
        print()

        if option == "1":
            vpc_name = input("Nombre de la VPC: ")
            cidr_block = input("Bloque CIDR: ")
            create_vpc(vpc_name, cidr_block)
            print()
        
        elif option == "2":
            list_vpcs()
            print()
        
        elif option == "3":
            vpc_name = input("Nombre de la VPC: ")
            cidr_block = input("Bloque CIDR: ")
            subnet_name = input("Nombre de la subred: ")
            delete_vpc(vpc_name, cidr_block, subnet_name)
            print()
        
        elif option in ["Q", "q"]:
            break

        else:
            print("Opcion no valida")
            print()



def menu_aws_vm():
    while True:
        print("Selecciona la operacion que deseas realizar:")
        print("1. Crear VM")
        print("2. Listar VMs")
        print("3. Operar VM")
        print("4. Eliminar VM")
        print("5. Crear par de claves SSH")
        print("6. Crear IP publica")
        print("7. Listar IPs publicas")
        print("8. Asignar IP publica")
        print("9. Desasignar IP publica")
        print("10. Eliminar IP publica")
        print("Q|q. Volver")
        option = input("Opcion >>> ")
        print()

        if option == "1":
            vm_name = input("Nombre de la VM: ")
            subnet_name = input("Nombre de la subred: ")
            vm_type = input("Tipo de VM: ")
            ami_selection = input("Nombre de la AMI (ubuntu, debian, amazon, win-server-22, win-server-19): ")
            key_name = input("Nombre del par de claves: ")
            if key_name not in list_key_pairs():
                print("Creando par de claves...")
                create_key_pair(key_name)
                print()
            create_vm(vm_name, vm_type, select_ami(ami_selection), get_subnet_id(subnet_name), key_name)
            print()
        
        elif option == "2":
            list_vms()
            print()
        
        elif option == "3":
            vm_name = input("Nombre de la maquina:")
            if vm_name in list_vm_names():
                print("Selecciona la operacion que deseas realizar:")
                print("1. Iniciar VM")
                print("2. Detener VM")
                print("3. Reiniciar VM")
                option2 = input("Opcion >>> ")
                print()

                if option2 == "1":
                    start_vm(get_vm_id(vm_name))
                if option2 == "2":
                    stop_vm(get_vm_id(vm_name))
                if option2 == "3":
                    stop_vm(get_vm_id(vm_name))
                    start_vm(get_vm_id(vm_name))
            else:
                print("No existe una maquina con ese nombre")
                print()
        
        elif option == "4":
            vm_name = input("Nombre de la maquina:")
            delete_vm(get_vm_id(vm_name))
            print()

        elif option == "5":
            key_name = input("Nombre del par de claves: ")
            create_key_pair(key_name)
            print()
        
        elif option == "6":
            ip_name = input("Nombre de la IP: ")
            create_ip(ip_name)
            print()
        
        elif option == "7":
            pass
            list_ips()
            print()

        elif option == "8":
            ip_name = input("Nombre de la IP: ")
            vm_name = input("Nombre de la maquina: ")
            attach_public_ip(ip_name, get_vm_id(vm_name))
            print()
        
        elif option == "9":
            vm_name = input("Nombre de la maquina: ")
            detach_public_ip(get_vm_id(vm_name))
            print()
        
        elif option == "10":
            ip_name = input("Nombre de la IP: ")
            delete_ip(get_ip_id(ip_name))
            print()
        
        elif option in ["Q", "q"]:
            break
            
        else:
            print("Opcion no valida")
            print()
        


def menu_aws_bucket():
    while True:
        print("Selecciona la operacion que deseas realizar:")
        print("1. Crear bucket")
        print("2. Listar buckets")
        print("3. Subir archivo a bucket")
        print("4. Descargar archivo de bucket")
        print("5. Configurar web estatica")
        print("6. Eliminar bucket")
        print("Q|q. Volver")
        option = input("Opcion >>> ")

        # TODO: Controlar errores del usuario antes de ejecutar funcion de aws
        if option == "1":
            bucket_name = input("Nombre del bucket: ")
            create_bucket(bucket_name)
            print()
        
        elif option == "2":
            pass
            list_buckets()
            print()
        
        elif option == "3":
            bucket_name = input("Nombre del bucket: ")
            file_name = input("Ruta del archivo: ")
            # TODO: Extraer nombre del fichero del string de la ruta
            upload_file_to_bucket(bucket_name, file_name, file_name.split("/")[-1])
            print()
        
        elif option == "4":
            bucket_name = input("Nombre del bucket: ")
            file_name = input("Nombre del archivo: ")
            download_file_from_bucket(bucket_name, file_name)
            print()
        
        elif option == "5":
            bucket_name = input("Nombre del bucket: ")
            file_name = input("Nombre del archivo: ")
            configure_web_bucket(bucket_name, file_name)
            print()
        
        elif option == "6":
            bucket_name = input("Nombre del bucket: ")
            delete_bucket(bucket_name)
            print()

        elif option in ["Q", "q"]:
            break
            
        else:
            print("Opcion no valida")
            print()
    


def menu_aws_dns():
    while True:
        print("Selecciona la operacion que deseas realizar:")
        print("1. Crear zona DNS")
        print("2. Listar zonas DNS")
        print("3. Crear registro DNS")
        print("4. Listar registros DNS")
        print("5. Eliminar registro DNS")
        print("6. Eliminar zona DNS")
        print("Q|q. Volver")
        option = input("Opcion >>> ")
        print()

        if option == "1":
            dns_name = input("Nombre de zona DNS: ")
            create_dns_zone(dns_name)
            print()
        
        elif option == "2":
            pass
            list_dns_zones()
            print()
        
        elif option == "3":
            zone_name = input("Nombre de la zona DNS: ")
            record_name = input("Nombre del registro: ")
            record_type = input("Tipo de registro: ")
            record_value = input("Valor del registro: ")
            create_dns_record(get_dns_zone_id(zone_name), record_name, record_type, record_value)
            print()
        
        elif option == "4":
            zone_name = input("Nombre de la zona DNS: ")
            list_dns_records(get_dns_zone_id(zone_name))
            print()
        
        elif option == "5":
            zone_name = input("Nombre de la zona DNS: ")
            record_name = input("Nombre del registro: ")
            record_type = input("Tipo de registro: ")
            delete_dns_record(get_dns_zone_id(zone_name), record_name, record_type)
            print()

        elif option == "6":
            zone_name = input("Nombre de la zona DNS: ")
            delete_dns_zone(get_dns_zone_id(zone_name))
            print()
        
        elif option in ["Q", "q"]:
            break

        else:
            print("Opcion no valida")
            print()



def menu_azure_vpc():
     while True:
        print("Selecciona la operacion que deseas realizar:")
        print("1. Crear VPC")
        print("2. Listar VPCs")
        print("3. Eliminar VPC")
        print("Q|q. Salir")
        option = input("Opcion >>> ")
        print()

        if option == "1":
            vpc_name = input("Nombre de la VPC: ")
            cidr_block = input("Bloque CIDR: ")
            subnet_name = input("Nombre de la subred: ")
            subnet_ip_block = input("Bloque CIDR de la subred: ")
            resources_group_name = input("Nombre del grupo de recursos: ")
            azure_create_vpc(vpc_name, cidr_block, subnet_name, subnet_ip_block, resources_group_name)
            print()
        
        elif option == "2":
            resources_group_name = input("Nombre del grupo de recursos: ")
            azure_list_vpcs(resources_group_name)
            print()
        
        elif option == "3":
            vpc_name = input("Nombre de la VPC: ")
            resources_group_name = input("Nombre del grupo de recursos: ")
            azure_delete_vpc(vpc_name, resources_group_name)
            print()
        
        elif option in ["Q", "q"]:
            break

        else:
            print("Opcion no valida")
            print()




def menu_azure_vm():
    while True:
        print("Selecciona la operacion que deseas realizar:")
        print("1. Crear VM")
        print("2. Operar VM")
        print("3. Eliminar VM")
        print("4. Crear IP publica")
        print("5. Asignar IP publica")
        print("6. Eliminar IP publica")
        print("Q|q. Volver")
        option = input("Opcion >>> ")
        print()

        if option == "1":
            vm_name = input("Nombre de la VM: ")
            vpc_name = input("Nombre de la red virtual: ")
            subnet_name = input("Nombre de la subred: ")
            azure_create_vm(vm_name, vpc_name, subnet_name)
            print()
        
        elif option == "2":
            vm_name = input("Nombre de la maquina:")
            resource_group = input("Nombre del grupo de recursos: ")
            print("Selecciona la operacion que deseas realizar:")
            print("1. Iniciar VM")
            print("2. Detener VM")
            print("3. Reiniciar VM")
            option2 = input("Opcion >>> ")
            print()

            if option2 == "1":
                azure_start_vm(resource_group, vm_name)
            if option2 == "2":
                azure_stop_vm(resource_group, vm_name)
            if option2 == "3":
                azure_stop_vm(resource_group, vm_name)
                azure_start_vm(resource_group, vm_name)

        
        elif option == "3":
            vm_name = input("Nombre de la maquina:")
            resource_group = input("Nombre del grupo de recursos: ")
            azure_delete_vm(resource_group, vm_name)
            print()

        elif option == "4":
            ip_name = input("Nombre de la IP: ")
            resource_group = input("Nombre del grupo de recursos: ")
            azure_create_ip(resource_group, ip_name)
            print()
        
        elif option == "5":
            ip_name = input("Nombre de la IP: ")
            nic_name = input("Nombre de la interfaz de red: ")
            resource_group = input("Nombre del grupo de recursos: ")
            azure_attach_ip(resource_group, nic_name, ip_name)
            print()
        
        elif option == "6":
            ip_name = input("Nombre de la IP: ")
            resource_group = input("Nombre del grupo de recursos: ")
            azure_delete_ip(resource_group, ip_name)
            print()
        
        elif option in ["Q", "q"]:
            break
            
        else:
            print("Opcion no valida")
            print()







menu_main()