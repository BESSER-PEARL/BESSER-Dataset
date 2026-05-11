





import java.util.List;
import java.util.ArrayList;

public class html_INPUT  {

    private String size;
    private String src;
    private String maxlength;
    private String inputValue;
    private String type;
    private String checked;
    private String align;
    private String name;



    public html_INPUT(
        String size,        String src,        String maxlength,        String inputValue,        String type,        String checked,        String align,        String name    ) {
        this.size = size;
        this.src = src;
        this.maxlength = maxlength;
        this.inputValue = inputValue;
        this.type = type;
        this.checked = checked;
        this.align = align;
        this.name = name;
    }


    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getMaxlength() {
        return maxlength;
    }

    public void setMaxlength(String maxlength) {
        this.maxlength = maxlength;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}