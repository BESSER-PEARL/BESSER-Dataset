





import java.util.List;
import java.util.ArrayList;

public class moba_MobaEnumLiteral  {

    private boolean default;
    private String literal;
    private boolean hidden;
    private String name;
    private boolean undefined;
    private int value;





    private moba_MobaEnum moba_mobaenum;


    public moba_MobaEnumLiteral(
        boolean default,        String literal,        boolean hidden,        String name,        boolean undefined,        int value    ) {
        this.default = default;
        this.literal = literal;
        this.hidden = hidden;
        this.name = name;
        this.undefined = undefined;
        this.value = value;
    }


    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }
    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }
    public boolean getHidden() {
        return hidden;
    }

    public void setHidden(boolean hidden) {
        this.hidden = hidden;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getUndefined() {
        return undefined;
    }

    public void setUndefined(boolean undefined) {
        this.undefined = undefined;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public moba_MobaEnum getMoba_mobaenum() {
        return moba_mobaenum;
    }

    public void setMoba_mobaenum(moba_MobaEnum moba_mobaenum) {
        this.moba_mobaenum = moba_mobaenum;
    }

}