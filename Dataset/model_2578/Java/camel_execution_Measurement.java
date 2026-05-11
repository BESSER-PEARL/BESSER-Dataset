




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class camel_execution_Measurement  {

    private String rawData;
    private LocalDate measurementTime;
    private String name;
    private float value;



    public camel_execution_Measurement(
        String rawData,        LocalDate measurementTime,        String name,        float value    ) {
        this.rawData = rawData;
        this.measurementTime = measurementTime;
        this.name = name;
        this.value = value;
    }


    public String getRawdata() {
        return rawData;
    }

    public void setRawdata(String rawData) {
        this.rawData = rawData;
    }
    public LocalDate getMeasurementtime() {
        return measurementTime;
    }

    public void setMeasurementtime(LocalDate measurementTime) {
        this.measurementTime = measurementTime;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }


}