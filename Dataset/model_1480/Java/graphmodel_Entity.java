





import java.util.List;
import java.util.ArrayList;

public class graphmodel_Entity  {

    private String text;
    private String name;
    private String y;
    private String category;
    private String ID;
    private String accessModifier;
    private String group;
    private String description;
    private String value;
    private String className;
    private String x;
    private String width;
    private String type;
    private String height;



    public graphmodel_Entity(
        String text,        String name,        String y,        String category,        String ID,        String accessModifier,        String group,        String description,        String value,        String className,        String x,        String width,        String type,        String height    ) {
        this.text = text;
        this.name = name;
        this.y = y;
        this.category = category;
        this.ID = ID;
        this.accessModifier = accessModifier;
        this.group = group;
        this.description = description;
        this.value = value;
        this.className = className;
        this.x = x;
        this.width = width;
        this.type = type;
        this.height = height;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getAccessmodifier() {
        return accessModifier;
    }

    public void setAccessmodifier(String accessModifier) {
        this.accessModifier = accessModifier;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getClassname() {
        return className;
    }

    public void setClassname(String className) {
        this.className = className;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }


}