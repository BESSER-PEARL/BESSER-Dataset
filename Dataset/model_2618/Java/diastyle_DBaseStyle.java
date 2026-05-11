





import java.util.List;
import java.util.ArrayList;

public class diastyle_DBaseStyle  {

    private String name;
    private String parentName;
    private String color;





    private diastyle_DBaseStyle diastyle_dbasestyle;




    private diastyle_DStyle diastyle_dstyle;


    public diastyle_DBaseStyle(
        String name,        String parentName,        String color    ) {
        this.name = name;
        this.parentName = parentName;
        this.color = color;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getParentname() {
        return parentName;
    }

    public void setParentname(String parentName) {
        this.parentName = parentName;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public diastyle_DBaseStyle getDiastyle_dbasestyle() {
        return diastyle_dbasestyle;
    }

    public void setDiastyle_dbasestyle(diastyle_DBaseStyle diastyle_dbasestyle) {
        this.diastyle_dbasestyle = diastyle_dbasestyle;
    }
    public diastyle_DStyle getDiastyle_dstyle() {
        return diastyle_dstyle;
    }

    public void setDiastyle_dstyle(diastyle_DStyle diastyle_dstyle) {
        this.diastyle_dstyle = diastyle_dstyle;
    }

}