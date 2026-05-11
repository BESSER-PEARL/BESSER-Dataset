





import java.util.List;
import java.util.ArrayList;

public class delphi_factor extends term {

    private String number;
    private String string;





    private delphi_expression delphi_expression;




    private delphi_typeId delphi_typeid;




    private delphi_expression delphi_expression;


    public delphi_factor(
        String number,        String string    ) {
        super(
        );
        this.number = number;
        this.string = string;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }

    public delphi_expression getDelphi_expression() {
        return delphi_expression;
    }

    public void setDelphi_expression(delphi_expression delphi_expression) {
        this.delphi_expression = delphi_expression;
    }
    public delphi_typeId getDelphi_typeid() {
        return delphi_typeid;
    }

    public void setDelphi_typeid(delphi_typeId delphi_typeid) {
        this.delphi_typeid = delphi_typeid;
    }
    public delphi_expression getDelphi_expression() {
        return delphi_expression;
    }

    public void setDelphi_expression(delphi_expression delphi_expression) {
        this.delphi_expression = delphi_expression;
    }

}