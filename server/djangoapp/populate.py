from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology"},
        {"name":"Mercedes", "description":"Good cars. German technology"},
        {"name":"Audi", "description":"Great cars. German technology"},
        {"name":"Kia", "description":"Good cars. Korean technology"},
        {"name":"Toyota", "description":"Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
            car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))


    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      {"name":"GTR", "type":"Sport", "year": 2026, "car_make":car_make_instances[0]},
      {"name":"Qashqai", "type":"SUV", "year": 2026, "car_make":car_make_instances[0]},
      {"name":"350Z", "type":"Sport", "year": 2026, "car_make":car_make_instances[0]},
      {"name":"S-Class", "type":"Sedan", "year": 2026, "car_make":car_make_instances[1]},
      {"name":"C-Class", "type":"Sedan", "year": 2026, "car_make":car_make_instances[1]},
      {"name":"A-Class", "type":"Hatchback", "year": 2026, "car_make":car_make_instances[1]},
      {"name":"RS4", "type":"Sedan", "year": 2026, "car_make":car_make_instances[2]},
      {"name":"RS5", "type":"SUV", "year": 2026, "car_make":car_make_instances[2]},
      {"name":"RS6", "type":"SUV", "year": 2026, "car_make":car_make_instances[2]},
      {"name":"Sorrento", "type":"SUV", "year": 2026, "car_make":car_make_instances[3]},
      {"name":"Stinger", "type":"SUV", "year": 2026, "car_make":car_make_instances[3]},
      {"name":"Cerato", "type":"Sedan", "year": 2026, "car_make":car_make_instances[3]},
      {"name":"Corolla", "type":"Sedan", "year": 2026, "car_make":car_make_instances[4]},
      {"name":"Camry", "type":"Sedan", "year": 2026, "car_make":car_make_instances[4]},
      {"name":"Supra", "type":"SUV", "year": 2026, "car_make":car_make_instances[4]},
        # Add more CarModel instances as needed
    ]

    for data in car_model_data:
            CarModel.objects.create(name=data['name'], car_make=data['car_make'], type=data['type'], year=data['year'])

