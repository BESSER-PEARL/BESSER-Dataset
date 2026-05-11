





import java.util.List;
import java.util.ArrayList;

public class HTML_INPUT  {

    private String name;
    private String align;
    private String src;
    private String maxlength;
    private String size;
    private String inputValue;
    private String type;
    private String checked;



    public HTML_INPUT(
        String name,        String align,        String src,        String maxlength,        String size,        String inputValue,        String type,        String checked    ) {
        this.name = name;
        this.align = align;
        this.src = src;
        this.maxlength = maxlength;
        this.size = size;
        this.inputValue = inputValue;
        this.type = type;
        this.checked = checked;
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
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
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


}