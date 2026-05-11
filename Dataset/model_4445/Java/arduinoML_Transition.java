





import java.util.List;
import java.util.ArrayList;

public class arduinoML_Transition  {

    private int a_values;
    private String comp;
    private String unit;
    private int time;
    private String d_values;





    private List<arduinoML_Digital> arduinoml_digitals;




    private List<arduinoML_Analog> arduinoml_analogs;


    public arduinoML_Transition(
        int a_values,        String comp,        String unit,        int time,        String d_values    ) {
        this.a_values = a_values;
        this.comp = comp;
        this.unit = unit;
        this.time = time;
        this.d_values = d_values;
        this.arduinoml_digitals = new ArrayList<>();
        this.arduinoml_analogs = new ArrayList<>();
    }

    public arduinoML_Transition(
        int a_values,        String comp,        String unit,        int time,        String d_values        ArrayList<arduinoML_Digital> arduinoml_digitals,        ArrayList<arduinoML_Analog> arduinoml_analogs    ) {
        this.a_values = a_values;
        this.comp = comp;
        this.unit = unit;
        this.time = time;
        this.d_values = d_values;
        this.arduinoml_digitals = arduinoml_digitals;
        this.arduinoml_analogs = arduinoml_analogs;
    }

    public int getA_values() {
        return a_values;
    }

    public void setA_values(int a_values) {
        this.a_values = a_values;
    }
    public String getComp() {
        return comp;
    }

    public void setComp(String comp) {
        this.comp = comp;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }
    public String getD_values() {
        return d_values;
    }

    public void setD_values(String d_values) {
        this.d_values = d_values;
    }

    public List<arduinoML_Digital> getArduinoml_digitals() {
        return arduinoml_digitals;
    }

    public void addArduinoml_digital(Arduinoml_digital arduinoml_digital) {
        this.arduinoml_digitals.add(arduinoml_digital);
    }
    public List<arduinoML_Analog> getArduinoml_analogs() {
        return arduinoml_analogs;
    }

    public void addArduinoml_analog(Arduinoml_analog arduinoml_analog) {
        this.arduinoml_analogs.add(arduinoml_analog);
    }

}