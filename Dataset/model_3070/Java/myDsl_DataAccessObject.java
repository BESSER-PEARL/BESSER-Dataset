





import java.util.List;
import java.util.ArrayList;

public class myDsl_DataAccessObject  {

    private String updateby;
    private String deleteby;
    private String findby;
    private String name;



    public myDsl_DataAccessObject(
        String updateby,        String deleteby,        String findby,        String name    ) {
        this.updateby = updateby;
        this.deleteby = deleteby;
        this.findby = findby;
        this.name = name;
    }


    public String getUpdateby() {
        return updateby;
    }

    public void setUpdateby(String updateby) {
        this.updateby = updateby;
    }
    public String getDeleteby() {
        return deleteby;
    }

    public void setDeleteby(String deleteby) {
        this.deleteby = deleteby;
    }
    public String getFindby() {
        return findby;
    }

    public void setFindby(String findby) {
        this.findby = findby;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}