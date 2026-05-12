





import java.util.List;
import java.util.ArrayList;

public class food_dish  {

    private String attribute2;
    private String type;
    private String attribute;





    private Component component;




    private List<menu> menus;




    private Component component;




    private List<Component> components;




    private menu menu;


    public food_dish(
        String attribute2,        String type,        String attribute    ) {
        this.attribute2 = attribute2;
        this.type = type;
        this.attribute = attribute;
        this.menus = new ArrayList<>();
        this.components = new ArrayList<>();
    }

    public food_dish(
        String attribute2,        String type,        String attribute        ArrayList<menu> menus,        ArrayList<Component> components    ) {
        this.attribute2 = attribute2;
        this.type = type;
        this.attribute = attribute;
        this.menus = menus;
        this.components = components;
    }

    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public Component getComponent() {
        return component;
    }

    public void setComponent(Component component) {
        this.component = component;
    }
    public List<menu> getMenus() {
        return menus;
    }

    public void addMenu(Menu menu) {
        this.menus.add(menu);
    }
    public Component getComponent() {
        return component;
    }

    public void setComponent(Component component) {
        this.component = component;
    }
    public List<Component> getComponents() {
        return components;
    }

    public void addComponent(Component component) {
        this.components.add(component);
    }
    public menu getMenu() {
        return menu;
    }

    public void setMenu(menu menu) {
        this.menu = menu;
    }

}