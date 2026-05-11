





import java.util.List;
import java.util.ArrayList;

public class robot_StatementBlock  {






    private robot_Robot robot_robot;




    private List<robot_Statement> robot_statements;




    private robot_ConditionalStatement robot_conditionalstatement;




    private robot_Scenario robot_scenario;


    public robot_StatementBlock(
    ) {
        this.robot_statements = new ArrayList<>();
    }

    public robot_StatementBlock(
        ArrayList<robot_Statement> robot_statements    ) {
        this.robot_statements = robot_statements;
    }


    public robot_Robot getRobot_robot() {
        return robot_robot;
    }

    public void setRobot_robot(robot_Robot robot_robot) {
        this.robot_robot = robot_robot;
    }
    public List<robot_Statement> getRobot_statements() {
        return robot_statements;
    }

    public void addRobot_statement(Robot_statement robot_statement) {
        this.robot_statements.add(robot_statement);
    }
    public robot_ConditionalStatement getRobot_conditionalstatement() {
        return robot_conditionalstatement;
    }

    public void setRobot_conditionalstatement(robot_ConditionalStatement robot_conditionalstatement) {
        this.robot_conditionalstatement = robot_conditionalstatement;
    }
    public robot_Scenario getRobot_scenario() {
        return robot_scenario;
    }

    public void setRobot_scenario(robot_Scenario robot_scenario) {
        this.robot_scenario = robot_scenario;
    }

}