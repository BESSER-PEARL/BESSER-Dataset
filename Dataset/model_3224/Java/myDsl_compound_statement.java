





import java.util.List;
import java.util.ArrayList;

public class myDsl_compound_statement  {






    private myDsl_function_definition mydsl_function_definition;




    private myDsl_statement mydsl_statement;




    private List<myDsl_block_item_list> mydsl_block_item_lists;


    public myDsl_compound_statement(
    ) {
        this.mydsl_block_item_lists = new ArrayList<>();
    }

    public myDsl_compound_statement(
        ArrayList<myDsl_block_item_list> mydsl_block_item_lists    ) {
        this.mydsl_block_item_lists = mydsl_block_item_lists;
    }


    public myDsl_function_definition getMydsl_function_definition() {
        return mydsl_function_definition;
    }

    public void setMydsl_function_definition(myDsl_function_definition mydsl_function_definition) {
        this.mydsl_function_definition = mydsl_function_definition;
    }
    public myDsl_statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }
    public List<myDsl_block_item_list> getMydsl_block_item_lists() {
        return mydsl_block_item_lists;
    }

    public void addMydsl_block_item_list(Mydsl_block_item_list mydsl_block_item_list) {
        this.mydsl_block_item_lists.add(mydsl_block_item_list);
    }

}