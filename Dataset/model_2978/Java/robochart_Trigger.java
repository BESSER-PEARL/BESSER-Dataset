





import java.util.List;
import java.util.ArrayList;

public class robochart_Trigger  {

    private String _type;





    private robochart_Expression robochart_expression;




    private robochart_SendEvent robochart_sendevent;




    private robochart_Variable robochart_variable;




    private robochart_Event robochart_event;




    private List<robochart_ClockReset> robochart_clockresets;




    private robochart_Variable robochart_variable;




    private robochart_Expression robochart_expression;




    private robochart_Variable robochart_variable;




    private robochart_Transition robochart_transition;


    public robochart_Trigger(
        String _type    ) {
        this._type = _type;
        this.robochart_clockresets = new ArrayList<>();
    }

    public robochart_Trigger(
        String _type        ArrayList<robochart_ClockReset> robochart_clockresets    ) {
        this._type = _type;
        this.robochart_clockresets = robochart_clockresets;
    }

    public String get_type() {
        return _type;
    }

    public void set_type(String _type) {
        this._type = _type;
    }

    public robochart_Expression getRobochart_expression() {
        return robochart_expression;
    }

    public void setRobochart_expression(robochart_Expression robochart_expression) {
        this.robochart_expression = robochart_expression;
    }
    public robochart_SendEvent getRobochart_sendevent() {
        return robochart_sendevent;
    }

    public void setRobochart_sendevent(robochart_SendEvent robochart_sendevent) {
        this.robochart_sendevent = robochart_sendevent;
    }
    public robochart_Variable getRobochart_variable() {
        return robochart_variable;
    }

    public void setRobochart_variable(robochart_Variable robochart_variable) {
        this.robochart_variable = robochart_variable;
    }
    public robochart_Event getRobochart_event() {
        return robochart_event;
    }

    public void setRobochart_event(robochart_Event robochart_event) {
        this.robochart_event = robochart_event;
    }
    public List<robochart_ClockReset> getRobochart_clockresets() {
        return robochart_clockresets;
    }

    public void addRobochart_clockreset(Robochart_clockreset robochart_clockreset) {
        this.robochart_clockresets.add(robochart_clockreset);
    }
    public robochart_Variable getRobochart_variable() {
        return robochart_variable;
    }

    public void setRobochart_variable(robochart_Variable robochart_variable) {
        this.robochart_variable = robochart_variable;
    }
    public robochart_Expression getRobochart_expression() {
        return robochart_expression;
    }

    public void setRobochart_expression(robochart_Expression robochart_expression) {
        this.robochart_expression = robochart_expression;
    }
    public robochart_Variable getRobochart_variable() {
        return robochart_variable;
    }

    public void setRobochart_variable(robochart_Variable robochart_variable) {
        this.robochart_variable = robochart_variable;
    }
    public robochart_Transition getRobochart_transition() {
        return robochart_transition;
    }

    public void setRobochart_transition(robochart_Transition robochart_transition) {
        this.robochart_transition = robochart_transition;
    }

}