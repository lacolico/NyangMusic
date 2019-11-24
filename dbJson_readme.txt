{
  "devices": [
    { // LED Module
      "id": 1,     // i
      "name": 3,   // LED_TYPE_A
      "type": 3,   // OUTPUT_MODULE
      "x": {
        "name": 1, // LED_RED
        "min": 0, 
        "max": 1   
      },
      "y": {
        "name": 2, // LED_Green
        "min": 0,
        "max": 1
      },
      "z": {
        "name": 3, // LED_Blue
        "min": 0,
        "max": 1
      },
      "w": {
        "name": 0, // UNUSED
        "min": 0,
        "max": 0
      }
    },
    { // Logic Module
      "id": 2,     // i
      "name": 2,   // LOGIC_TYPE_A
      "type": 2,   // LOGIC_MODULE
      "x": {
        "name": 8, // LOGIC_MODE
        "min": 0, 
        "max": 2  
      },
      "y": {
        "name": 0, // UNUSED
        "min": 0,
        "max": 0
      },
      "z": {
        "name": 0, // UNUSED
        "min": 0,
        "max": 0
      },
      "w": {
        "name": 0, // UNUSED
        "min": 0,
        "max": 0
      }
    },
    { // Motion Module
      "id": 3,     // i
      "name": 6,   // MOTION_TYPE_A
      "type": 4,   // INPUT_MODULE
      "x": {
        "name": 7, // MOTION_FIND
        "min": 0, 
        "max": 1   
      },
      "y": {
        "name": 0, // UNUSED
        "min": 0,
        "max": 0
      },
      "z": {
        "name": 0, // UNUSED
        "min": 0,
        "max": 0
      },
      "w": {
        "name": 0, // UNUSED
        "min": 0,
        "max": 0
      }
    },
    { // Temphumi Module
      "id": 4,     // i
      "name": 5,   // TEMPHUMI_TYPE_A
      "type": 4,   // INPUT_MODULE
      "x": {
        "name": 5, // TEMPHUMI_TEMPERATURE
        "min": 0, 
        "max": 50   
      },
      "y": {
        "name": 6, // TEMPHUMI_HUMIDITY
        "min": 20,
        "max": 90
      },
      "z": {
        "name": 0, // UNUSED
        "min": 0,
        "max": 0
      },
      "w": {
        "name": 0, // UNUSED
        "min": 0,
        "max": 0
      }
    }
  ],
  "event": {
    "result_msg": 1 // 0: Error, 1: Success 
  },
  "is_change": {
    "result_msg" : 0 // 0: No, 1: Yes
  },
  "module_count": {
    "result_msg": 4 // Module Count
  },
  "now_mode" : {
    "result_msg": 1 // 0: project, 1: logic
  }
}
