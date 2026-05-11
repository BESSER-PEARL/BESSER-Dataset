





import java.util.List;
import java.util.ArrayList;

public class kernel_statements_ParallelBlock extends statements_StatementListContainer, statements_Statement {

    private String order;



    public kernel_statements_ParallelBlock(
        String order    ) {
        super(
        );
        this.order = order;
    }


    public String getOrder() {
        return order;
    }

    public void setOrder(String order) {
        this.order = order;
    }


}