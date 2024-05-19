#Zadanie 3

def licz_sume(input_dict):

    total_knuts = sum(input_dict.get("knut", []))
    total_sykls = sum(input_dict.get("sykl", []))
    total_galeons = sum(input_dict.get("galeon", []))
    
    total_sykls += total_knuts // 21
    remaining_knuts = total_knuts % 21
    
    total_galeons += total_sykls // 17
    remaining_sykls = total_sykls % 17
    
    output_dict = {
        "galeon": total_galeons,
        "sykl": remaining_sykls,
        "knut": remaining_knuts
    }
    
    return output_dict

