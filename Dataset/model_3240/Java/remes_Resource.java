





import java.util.List;
import java.util.ArrayList;

public class remes_Resource extends Referable {

    private String type;
    private String expression;





    private remes_Mode remes_mode;




    private remes_Mode remes_mode;


    public remes_Resource(
        String type,        String expression    ) {
        super(
        );
        this.type = type;
        this.expression = expression;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }

    public remes_Mode getRemes_mode() {
        return remes_mode;
    }

    public void setRemes_mode(remes_Mode remes_mode) {
        this.remes_mode = remes_mode;
    }
    public remes_Mode getRemes_mode() {
        return remes_mode;
    }

    public void setRemes_mode(remes_Mode remes_mode) {
        this.remes_mode = remes_mode;
    }

}