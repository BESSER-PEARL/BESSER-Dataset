





import java.util.List;
import java.util.ArrayList;

public class List_List  {

    private int size;
    private String type;





    private Test test;




    private List_List list_list;


    public List_List(
        int size,        String type    ) {
        this.size = size;
        this.type = type;
        this.list_lists = new ArrayList<>();
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public Test getTest() {
        return test;
    }

    public void setTest(Test test) {
        this.test = test;
    }
    public List_List getList_lists() {
        return list_lists;
    }

    public void addList_list(List_list list_list) {
        this.list_lists.add(list_list);
    }

}