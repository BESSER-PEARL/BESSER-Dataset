





import java.util.List;
import java.util.ArrayList;

public class graphmodelling_Entity  {

    private String x;
    private String className;
    private String description;
    private String accessModifier;
    private String category;
    private String group;
    private String height;
    private String value;
    private String ID;
    private String y;
    private String text;
    private String type;
    private String name;
    private String width;



    public graphmodelling_Entity(
        String x,        String className,        String description,        String accessModifier,        String category,        String group,        String height,        String value,        String ID,        String y,        String text,        String type,        String name,        String width    ) {
        this.x = x;
        this.className = className;
        this.description = description;
        this.accessModifier = accessModifier;
        this.category = category;
        this.group = group;
        this.height = height;
        this.value = value;
        this.ID = ID;
        this.y = y;
        this.text = text;
        this.type = type;
        this.name = name;
        this.width = width;
    }


    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getAccessmodifier() {
        return accessModifier;
    }

    public void setAccessmodifier(String accessModifier) {
        this.accessModifier = accessModifier;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }


}