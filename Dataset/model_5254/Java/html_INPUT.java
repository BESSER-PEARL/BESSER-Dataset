





import java.util.List;
import java.util.ArrayList;

public class html_INPUT  {

    private String maxlength;
    private String name;
    private String src;
    private String checked;
    private String align;
    private String inputValue;
    private String type;
    private String size;



    public html_INPUT(
        String maxlength,        String name,        String src,        String checked,        String align,        String inputValue,        String type,        String size    ) {
        this.maxlength = maxlength;
        this.name = name;
        this.src = src;
        this.checked = checked;
        this.align = align;
        this.inputValue = inputValue;
        this.type = type;
        this.size = size;
    }


    public String getMaxlength() {
        return maxlength;
    }

    public void setMaxlength(String maxlength) {
        this.maxlength = maxlength;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getChecked() {
        return checked;
    }

    public void setChecked(String checked) {
        this.checked = checked;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getInputvalue() {
        return inputValue;
    }

    public void setInputvalue(String inputValue) {
        this.inputValue = inputValue;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }


}