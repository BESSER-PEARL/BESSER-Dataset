





import java.util.List;
import java.util.ArrayList;

public class iot2_Expression extends Statement_FunctioncallOrAssignment {






    private iot2_Expression_Length iot2_expression_length;




    private iot2_OpaqueAction iot2_opaqueaction;




    private iot2_Expression_AccessArray iot2_expression_accessarray;




    private iot2_Expression_Negate iot2_expression_negate;




    private iot2_Expression_AccessArray iot2_expression_accessarray;




    private iot2_Expression_CallFunction iot2_expression_callfunction;




    private iot2_Expression_CallMemberFunction iot2_expression_callmemberfunction;




    private iot2_Expression_AccessMember iot2_expression_accessmember;




    private iot2_Field iot2_field;


    public iot2_Expression(
    ) {
        super(
        );
    }



    public iot2_Expression_Length getIot2_expression_length() {
        return iot2_expression_length;
    }

    public void setIot2_expression_length(iot2_Expression_Length iot2_expression_length) {
        this.iot2_expression_length = iot2_expression_length;
    }
    public iot2_OpaqueAction getIot2_opaqueaction() {
        return iot2_opaqueaction;
    }

    public void setIot2_opaqueaction(iot2_OpaqueAction iot2_opaqueaction) {
        this.iot2_opaqueaction = iot2_opaqueaction;
    }
    public iot2_Expression_AccessArray getIot2_expression_accessarray() {
        return iot2_expression_accessarray;
    }

    public void setIot2_expression_accessarray(iot2_Expression_AccessArray iot2_expression_accessarray) {
        this.iot2_expression_accessarray = iot2_expression_accessarray;
    }
    public iot2_Expression_Negate getIot2_expression_negate() {
        return iot2_expression_negate;
    }

    public void setIot2_expression_negate(iot2_Expression_Negate iot2_expression_negate) {
        this.iot2_expression_negate = iot2_expression_negate;
    }
    public iot2_Expression_AccessArray getIot2_expression_accessarray() {
        return iot2_expression_accessarray;
    }

    public void setIot2_expression_accessarray(iot2_Expression_AccessArray iot2_expression_accessarray) {
        this.iot2_expression_accessarray = iot2_expression_accessarray;
    }
    public iot2_Expression_CallFunction getIot2_expression_callfunction() {
        return iot2_expression_callfunction;
    }

    public void setIot2_expression_callfunction(iot2_Expression_CallFunction iot2_expression_callfunction) {
        this.iot2_expression_callfunction = iot2_expression_callfunction;
    }
    public iot2_Expression_CallMemberFunction getIot2_expression_callmemberfunction() {
        return iot2_expression_callmemberfunction;
    }

    public void setIot2_expression_callmemberfunction(iot2_Expression_CallMemberFunction iot2_expression_callmemberfunction) {
        this.iot2_expression_callmemberfunction = iot2_expression_callmemberfunction;
    }
    public iot2_Expression_AccessMember getIot2_expression_accessmember() {
        return iot2_expression_accessmember;
    }

    public void setIot2_expression_accessmember(iot2_Expression_AccessMember iot2_expression_accessmember) {
        this.iot2_expression_accessmember = iot2_expression_accessmember;
    }
    public iot2_Field getIot2_field() {
        return iot2_field;
    }

    public void setIot2_field(iot2_Field iot2_field) {
        this.iot2_field = iot2_field;
    }

}