





import java.util.List;
import java.util.ArrayList;

public class tdt4250_Assignment  {

    private int ID;
    private String name;
    private boolean mandatory;
    private String content;



    public tdt4250_Assignment(
        int ID,        String name,        boolean mandatory,        String content    ) {
        this.ID = ID;
        this.name = name;
        this.mandatory = mandatory;
        this.content = content;
    }


    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }


}