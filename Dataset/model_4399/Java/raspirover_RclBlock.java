





import java.util.List;
import java.util.ArrayList;

public class raspirover_RclBlock extends Statement {






    private raspirover_Statement raspirover_statement;




    private List<raspirover_Statement> raspirover_statements;




    private raspirover_Conditional raspirover_conditional;




    private raspirover_Conditional raspirover_conditional;




    private raspirover_RoverProgram raspirover_roverprogram;


    public raspirover_RclBlock(
    ) {
        super(
        );
        this.raspirover_statements = new ArrayList<>();
    }

    public raspirover_RclBlock(
        ArrayList<raspirover_Statement> raspirover_statements    ) {
        this.raspirover_statements = raspirover_statements;
    }


    public raspirover_Statement getRaspirover_statement() {
        return raspirover_statement;
    }

    public void setRaspirover_statement(raspirover_Statement raspirover_statement) {
        this.raspirover_statement = raspirover_statement;
    }
    public List<raspirover_Statement> getRaspirover_statements() {
        return raspirover_statements;
    }

    public void addRaspirover_statement(Raspirover_statement raspirover_statement) {
        this.raspirover_statements.add(raspirover_statement);
    }
    public raspirover_Conditional getRaspirover_conditional() {
        return raspirover_conditional;
    }

    public void setRaspirover_conditional(raspirover_Conditional raspirover_conditional) {
        this.raspirover_conditional = raspirover_conditional;
    }
    public raspirover_Conditional getRaspirover_conditional() {
        return raspirover_conditional;
    }

    public void setRaspirover_conditional(raspirover_Conditional raspirover_conditional) {
        this.raspirover_conditional = raspirover_conditional;
    }
    public raspirover_RoverProgram getRaspirover_roverprogram() {
        return raspirover_roverprogram;
    }

    public void setRaspirover_roverprogram(raspirover_RoverProgram raspirover_roverprogram) {
        this.raspirover_roverprogram = raspirover_roverprogram;
    }

}