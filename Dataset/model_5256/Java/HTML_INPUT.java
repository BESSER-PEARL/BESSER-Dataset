





import java.util.List;
import java.util.ArrayList;

public class HTML_INPUT  {

    private String inputValue;
    private String src;
    private String maxlength;
    private String type;
    private String align;
    private String size;
    private String name;
    private String checked;



    public HTML_INPUT(
        String inputValue,        String src,        String maxlength,        String type,        String align,        String size,        String name,        String checked    ) {
        this.inputValue = inputValue;
        this.src = src;
        this.maxlength = maxlength;
        this.type = type;
        this.align = align;
        this.size = size;
        this.name = name;
        this.checked = checked;
    }


    public String getInputvalue() {
        return inputValue;
    }

    public void setInputvalue(String inputValue) {
        this.inputValue = inputValue;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
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
    public String getChecked() {
        return checked;
    }

    public void setChecked(String checked) {
        this.checked = checked;
    }


}