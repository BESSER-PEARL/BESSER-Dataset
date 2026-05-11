





import java.util.List;
import java.util.ArrayList;

public class sadl_Range  {

    private String list;
    private String lists;
    private String single;





    private sadl_AddlClassInfo sadl_addlclassinfo;


    public sadl_Range(
        String list,        String lists,        String single    ) {
        this.list = list;
        this.lists = lists;
        this.single = single;
    }


    public String getList() {
        return list;
    }

    public void setList(String list) {
        this.list = list;
    }
    public String getLists() {
        return lists;
    }

    public void setLists(String lists) {
        this.lists = lists;
    }
    public String getSingle() {
        return single;
    }

    public void setSingle(String single) {
        this.single = single;
    }

    public sadl_AddlClassInfo getSadl_addlclassinfo() {
        return sadl_addlclassinfo;
    }

    public void setSadl_addlclassinfo(sadl_AddlClassInfo sadl_addlclassinfo) {
        this.sadl_addlclassinfo = sadl_addlclassinfo;
    }

}