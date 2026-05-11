




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class bank_Transaction  {

    private String id;
    private String amount;
    private LocalDate date;
    private String comment;





    private bank_TransactionInitiator bank_transactioninitiator;




    private bank_Statement bank_statement;




    private bank_Statement bank_statement;


    public bank_Transaction(
        String id,        String amount,        LocalDate date,        String comment    ) {
        this.id = id;
        this.amount = amount;
        this.date = date;
        this.comment = comment;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public bank_TransactionInitiator getBank_transactioninitiator() {
        return bank_transactioninitiator;
    }

    public void setBank_transactioninitiator(bank_TransactionInitiator bank_transactioninitiator) {
        this.bank_transactioninitiator = bank_transactioninitiator;
    }
    public bank_Statement getBank_statement() {
        return bank_statement;
    }

    public void setBank_statement(bank_Statement bank_statement) {
        this.bank_statement = bank_statement;
    }
    public bank_Statement getBank_statement() {
        return bank_statement;
    }

    public void setBank_statement(bank_Statement bank_statement) {
        this.bank_statement = bank_statement;
    }

}