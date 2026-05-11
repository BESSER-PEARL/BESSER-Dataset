





import java.util.List;
import java.util.ArrayList;

public class html_INPUT  {

    private String src;
    private String inputValue;
    private String type;
    private String size;
    private String name;
    private String align;
    private String checked;
    private String maxlength;



    public html_INPUT(
        String src,        String inputValue,        String type,        String size,        String name,        String align,        String checked,        String maxlength    ) {
        this.src = src;
        this.inputValue = inputValue;
        this.type = type;
        this.size = size;
        this.name = name;
        this.align = align;
        this.checked = checked;
        this.maxlength = maxlength;
    }


    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getChecked() {
        return checked;
    }

    public void setChecked(String checked) {
        this.checked = checked;
    }
    public String getMaxlength() {
        return maxlength;
    }

    public void setMaxlength(String maxlength) {
        this.maxlength = maxlength;
    }


}