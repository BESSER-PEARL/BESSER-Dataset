





import java.util.List;
import java.util.ArrayList;

public class codetaginfo_CodeTagContext  {

    private String operation_name;
    private String group;
    private String component_name;
    private String class_name;





    private codetaginfo_CodeTag codetaginfo_codetag;


    public codetaginfo_CodeTagContext(
        String operation_name,        String group,        String component_name,        String class_name    ) {
        this.operation_name = operation_name;
        this.group = group;
        this.component_name = component_name;
        this.class_name = class_name;
    }


    public String getOperation_name() {
        return operation_name;
    }

    public void setOperation_name(String operation_name) {
        this.operation_name = operation_name;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getComponent_name() {
        return component_name;
    }

    public void setComponent_name(String component_name) {
        this.component_name = component_name;
    }
    public String getClass_name() {
        return class_name;
    }

    public void setClass_name(String class_name) {
        this.class_name = class_name;
    }

    public codetaginfo_CodeTag getCodetaginfo_codetag() {
        return codetaginfo_codetag;
    }

    public void setCodetaginfo_codetag(codetaginfo_CodeTag codetaginfo_codetag) {
        this.codetaginfo_codetag = codetaginfo_codetag;
    }

}