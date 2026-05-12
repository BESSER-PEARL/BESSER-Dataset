





import java.util.List;
import java.util.ArrayList;

public class Catering  {

    private String attribute;
    private String Menu;



    public Catering(
        String attribute,        String Menu    ) {
        this.attribute = attribute;
        this.Menu = Menu;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getMenu() {
        return Menu;
    }

    public void setMenu(String Menu) {
        this.Menu = Menu;
    }


}