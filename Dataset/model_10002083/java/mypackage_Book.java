





import java.util.List;
import java.util.ArrayList;

public class mypackage_Book  {

    private String BId;
    private String BName;
    private String Price;





    private mypackage_Course mypackage_course;




    private mypackage_FileManager mypackage_filemanager;


    public mypackage_Book(
        String BId,        String BName,        String Price    ) {
        this.BId = BId;
        this.BName = BName;
        this.Price = Price;
    }


    public String getBid() {
        return BId;
    }

    public void setBid(String BId) {
        this.BId = BId;
    }
    public String getBname() {
        return BName;
    }

    public void setBname(String BName) {
        this.BName = BName;
    }
    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }

    public mypackage_Course getMypackage_course() {
        return mypackage_course;
    }

    public void setMypackage_course(mypackage_Course mypackage_course) {
        this.mypackage_course = mypackage_course;
    }
    public mypackage_FileManager getMypackage_filemanager() {
        return mypackage_filemanager;
    }

    public void setMypackage_filemanager(mypackage_FileManager mypackage_filemanager) {
        this.mypackage_filemanager = mypackage_filemanager;
    }

}