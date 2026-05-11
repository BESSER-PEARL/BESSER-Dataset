





import java.util.List;
import java.util.ArrayList;

public class xal_DepartmentName  {

    private String anyAttribute;
    private String code;
    private String mixed;
    private String type;





    private xal_Department xal_department;


    public xal_DepartmentName(
        String anyAttribute,        String code,        String mixed,        String type    ) {
        this.anyAttribute = anyAttribute;
        this.code = code;
        this.mixed = mixed;
        this.type = type;
    }


    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public xal_Department getXal_department() {
        return xal_department;
    }

    public void setXal_department(xal_Department xal_department) {
        this.xal_department = xal_department;
    }

}