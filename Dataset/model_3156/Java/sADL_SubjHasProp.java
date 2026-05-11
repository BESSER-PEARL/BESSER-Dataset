





import java.util.List;
import java.util.ArrayList;

public class sADL_SubjHasProp extends Expression {

    private boolean comma;





    private sADL_Expression sadl_expression;




    private sADL_SadlResource sadl_sadlresource;




    private sADL_Expression sadl_expression;


    public sADL_SubjHasProp(
        boolean comma    ) {
        super(
        );
        this.comma = comma;
    }


    public boolean getComma() {
        return comma;
    }

    public void setComma(boolean comma) {
        this.comma = comma;
    }

    public sADL_Expression getSadl_expression() {
        return sadl_expression;
    }

    public void setSadl_expression(sADL_Expression sadl_expression) {
        this.sadl_expression = sadl_expression;
    }
    public sADL_SadlResource getSadl_sadlresource() {
        return sadl_sadlresource;
    }

    public void setSadl_sadlresource(sADL_SadlResource sadl_sadlresource) {
        this.sadl_sadlresource = sadl_sadlresource;
    }
    public sADL_Expression getSadl_expression() {
        return sadl_expression;
    }

    public void setSadl_expression(sADL_Expression sadl_expression) {
        this.sadl_expression = sadl_expression;
    }

}