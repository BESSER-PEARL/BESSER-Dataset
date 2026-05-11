





import java.util.List;
import java.util.ArrayList;

public class myDsl_declaration  {






    private myDsl_external_declaration mydsl_external_declaration;




    private myDsl_iteration_statement mydsl_iteration_statement;




    private myDsl_block_item mydsl_block_item;


    public myDsl_declaration(
    ) {
    }



    public myDsl_external_declaration getMydsl_external_declaration() {
        return mydsl_external_declaration;
    }

    public void setMydsl_external_declaration(myDsl_external_declaration mydsl_external_declaration) {
        this.mydsl_external_declaration = mydsl_external_declaration;
    }
    public myDsl_iteration_statement getMydsl_iteration_statement() {
        return mydsl_iteration_statement;
    }

    public void setMydsl_iteration_statement(myDsl_iteration_statement mydsl_iteration_statement) {
        this.mydsl_iteration_statement = mydsl_iteration_statement;
    }
    public myDsl_block_item getMydsl_block_item() {
        return mydsl_block_item;
    }

    public void setMydsl_block_item(myDsl_block_item mydsl_block_item) {
        this.mydsl_block_item = mydsl_block_item;
    }

}