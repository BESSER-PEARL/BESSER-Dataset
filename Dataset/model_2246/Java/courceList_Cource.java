





import java.util.List;
import java.util.ArrayList;

public class courceList_Cource  {

    private String name;
    private String code;
    private String location;





    private courceList_Department courcelist_department;




    private courceList_Department courcelist_department;


    public courceList_Cource(
        String name,        String code,        String location    ) {
        this.name = name;
        this.code = code;
        this.location = location;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public courceList_Department getCourcelist_department() {
        return courcelist_department;
    }

    public void setCourcelist_department(courceList_Department courcelist_department) {
        this.courcelist_department = courcelist_department;
    }
    public courceList_Department getCourcelist_department() {
        return courcelist_department;
    }

    public void setCourcelist_department(courceList_Department courcelist_department) {
        this.courcelist_department = courcelist_department;
    }

}