





import java.util.List;
import java.util.ArrayList;

public class aml_Value  {

    private String mixed;
    private String unit;
    private String type;
    private String group;





    private aml_DocumentRoot aml_documentroot;




    private List<aml_List> aml_lists;




    private aml_Parameter aml_parameter;




    private List<aml_Interval> aml_intervals;


    public aml_Value(
        String mixed,        String unit,        String type,        String group    ) {
        this.mixed = mixed;
        this.unit = unit;
        this.type = type;
        this.group = group;
        this.aml_lists = new ArrayList<>();
        this.aml_intervals = new ArrayList<>();
    }

    public aml_Value(
        String mixed,        String unit,        String type,        String group        ArrayList<aml_List> aml_lists,        ArrayList<aml_Interval> aml_intervals    ) {
        this.mixed = mixed;
        this.unit = unit;
        this.type = type;
        this.group = group;
        this.aml_lists = aml_lists;
        this.aml_intervals = aml_intervals;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public aml_DocumentRoot getAml_documentroot() {
        return aml_documentroot;
    }

    public void setAml_documentroot(aml_DocumentRoot aml_documentroot) {
        this.aml_documentroot = aml_documentroot;
    }
    public List<aml_List> getAml_lists() {
        return aml_lists;
    }

    public void addAml_list(Aml_list aml_list) {
        this.aml_lists.add(aml_list);
    }
    public aml_Parameter getAml_parameter() {
        return aml_parameter;
    }

    public void setAml_parameter(aml_Parameter aml_parameter) {
        this.aml_parameter = aml_parameter;
    }
    public List<aml_Interval> getAml_intervals() {
        return aml_intervals;
    }

    public void addAml_interval(Aml_interval aml_interval) {
        this.aml_intervals.add(aml_interval);
    }

}