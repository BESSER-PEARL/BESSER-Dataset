





import java.util.List;
import java.util.ArrayList;

public class aml_Value  {

    private String mixed;
    private String group;
    private String type;
    private String unit;





    private List<aml_Interval> aml_intervals;




    private List<aml_List> aml_lists;




    private aml_Parameter aml_parameter;




    private aml_DocumentRoot aml_documentroot;


    public aml_Value(
        String mixed,        String group,        String type,        String unit    ) {
        this.mixed = mixed;
        this.group = group;
        this.type = type;
        this.unit = unit;
        this.aml_intervals = new ArrayList<>();
        this.aml_lists = new ArrayList<>();
    }

    public aml_Value(
        String mixed,        String group,        String type,        String unit        ArrayList<aml_Interval> aml_intervals,        ArrayList<aml_List> aml_lists    ) {
        this.mixed = mixed;
        this.group = group;
        this.type = type;
        this.unit = unit;
        this.aml_intervals = aml_intervals;
        this.aml_lists = aml_lists;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }

    public List<aml_Interval> getAml_intervals() {
        return aml_intervals;
    }

    public void addAml_interval(Aml_interval aml_interval) {
        this.aml_intervals.add(aml_interval);
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
    public aml_DocumentRoot getAml_documentroot() {
        return aml_documentroot;
    }

    public void setAml_documentroot(aml_DocumentRoot aml_documentroot) {
        this.aml_documentroot = aml_documentroot;
    }

}