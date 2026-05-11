





import java.util.List;
import java.util.ArrayList;

public class defaultname_INPUT  {

    private String inputValue;
    private String checked;
    private String maxlength;
    private String name;
    private String src;
    private String align;
    private String size;
    private String type;



    public defaultname_INPUT(
        String inputValue,        String checked,        String maxlength,        String name,        String src,        String align,        String size,        String type    ) {
        this.inputValue = inputValue;
        this.checked = checked;
        this.maxlength = maxlength;
        this.name = name;
        this.src = src;
        this.align = align;
        this.size = size;
        this.type = type;
    }


    public String getInputvalue() {
        return inputValue;
    }

    public void setInputvalue(String inputValue) {
        this.inputValue = inputValue;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}