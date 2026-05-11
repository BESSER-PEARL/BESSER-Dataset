





import java.util.List;
import java.util.ArrayList;

public class myDsl_compound_statement  {






    private List<myDsl_block_item> mydsl_block_items;




    private myDsl_statement mydsl_statement;


    public myDsl_compound_statement(
    ) {
        this.mydsl_block_items = new ArrayList<>();
    }

    public myDsl_compound_statement(
        ArrayList<myDsl_block_item> mydsl_block_items    ) {
        this.mydsl_block_items = mydsl_block_items;
    }


    public List<myDsl_block_item> getMydsl_block_items() {
        return mydsl_block_items;
    }

    public void addMydsl_block_item(Mydsl_block_item mydsl_block_item) {
        this.mydsl_block_items.add(mydsl_block_item);
    }
    public myDsl_statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }

}