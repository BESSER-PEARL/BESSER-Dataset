





import java.util.List;
import java.util.ArrayList;

public class Matching  {

    private String answer;
    private String col1__col2;
    private String question;
    private String c1__c2__c3__c4;
    private boolean multians;



    public Matching(
        String answer,        String col1__col2,        String question,        String c1__c2__c3__c4,        boolean multians    ) {
        this.answer = answer;
        this.col1__col2 = col1__col2;
        this.question = question;
        this.c1__c2__c3__c4 = c1__c2__c3__c4;
        this.multians = multians;
    }


    public String getAnswer() {
        return answer;
    }

    public void setAnswer(String answer) {
        this.answer = answer;
    }
    public String getCol1__col2() {
        return col1__col2;
    }

    public void setCol1__col2(String col1__col2) {
        this.col1__col2 = col1__col2;
    }
    public String getQuestion() {
        return question;
    }

    public void setQuestion(String question) {
        this.question = question;
    }
    public String getC1__c2__c3__c4() {
        return c1__c2__c3__c4;
    }

    public void setC1__c2__c3__c4(String c1__c2__c3__c4) {
        this.c1__c2__c3__c4 = c1__c2__c3__c4;
    }
    public boolean getMultians() {
        return multians;
    }

    public void setMultians(boolean multians) {
        this.multians = multians;
    }


}