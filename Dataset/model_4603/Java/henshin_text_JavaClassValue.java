





import java.util.List;
import java.util.ArrayList;

public class henshin_text_JavaClassValue extends Expression {

    private String value;





    private List<henshin_text_Expression> henshin_text_expressions;


    public henshin_text_JavaClassValue(
        String value    ) {
        super(
        );
        this.value = value;
        this.henshin_text_expressions = new ArrayList<>();
    }

    public henshin_text_JavaClassValue(
        String value        ArrayList<henshin_text_Expression> henshin_text_expressions    ) {
        this.value = value;
        this.henshin_text_expressions = henshin_text_expressions;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public List<henshin_text_Expression> getHenshin_text_expressions() {
        return henshin_text_expressions;
    }

    public void addHenshin_text_expression(Henshin_text_expression henshin_text_expression) {
        this.henshin_text_expressions.add(henshin_text_expression);
    }

}