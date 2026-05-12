





import java.util.List;
import java.util.ArrayList;

public class Catering  {

    private String get_menu;
    private String get_cost;



    public Catering(
        String get_menu,        String get_cost    ) {
        this.get_menu = get_menu;
        this.get_cost = get_cost;
    }


    public String getGet_menu() {
        return get_menu;
    }

    public void setGet_menu(String get_menu) {
        this.get_menu = get_menu;
    }
    public String getGet_cost() {
        return get_cost;
    }

    public void setGet_cost(String get_cost) {
        this.get_cost = get_cost;
    }


}