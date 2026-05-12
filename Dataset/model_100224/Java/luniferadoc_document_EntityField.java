





import java.util.List;
import java.util.ArrayList;

public class luniferadoc_document_EntityField  {

    private int length;
    private boolean nullable;
    private String name;
    private String type;
    private boolean pk;





    private RichString richstring;


    public luniferadoc_document_EntityField(
        int length,        boolean nullable,        String name,        String type,        boolean pk    ) {
        this.length = length;
        this.nullable = nullable;
        this.name = name;
        this.type = type;
        this.pk = pk;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public boolean getNullable() {
        return nullable;
    }

    public void setNullable(boolean nullable) {
        this.nullable = nullable;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getPk() {
        return pk;
    }

    public void setPk(boolean pk) {
        this.pk = pk;
    }

    public RichString getRichstring() {
        return richstring;
    }

    public void setRichstring(RichString richstring) {
        this.richstring = richstring;
    }

}