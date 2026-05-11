





import java.util.List;
import java.util.ArrayList;

public class myDsl_block_item  {






    private myDsl_statement mydsl_statement;




    private myDsl_block_item_list mydsl_block_item_list;


    public myDsl_block_item(
    ) {
    }



    public myDsl_statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }
    public myDsl_block_item_list getMydsl_block_item_list() {
        return mydsl_block_item_list;
    }

    public void setMydsl_block_item_list(myDsl_block_item_list mydsl_block_item_list) {
        this.mydsl_block_item_list = mydsl_block_item_list;
    }

}