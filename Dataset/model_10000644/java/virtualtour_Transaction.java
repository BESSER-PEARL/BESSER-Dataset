




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class virtualtour_Transaction  {

    private int id;
    private LocalDate transactionTime;
    private None type;



    public virtualtour_Transaction(
        int id,        LocalDate transactionTime,        None type    ) {
        this.id = id;
        this.transactionTime = transactionTime;
        this.type = type;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDate getTransactiontime() {
        return transactionTime;
    }

    public void setTransactiontime(LocalDate transactionTime) {
        this.transactionTime = transactionTime;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }


}