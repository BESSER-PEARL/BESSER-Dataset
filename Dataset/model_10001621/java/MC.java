





import java.util.List;
import java.util.ArrayList;

public class MC  {

    private String question;
    private String answer;
    private String c1__c2__c3__c4;
    private boolean multians;



    public MC(
        String question,        String answer,        String c1__c2__c3__c4,        boolean multians    ) {
        this.question = question;
        this.answer = answer;
        this.c1__c2__c3__c4 = c1__c2__c3__c4;
        this.multians = multians;
    }


    public String getQuestion() {
        return question;
    }

    public void setQuestion(String question) {
        this.question = question;
    }
    public String getAnswer() {
        return answer;
    }

    public void setAnswer(String answer) {
        this.answer = answer;
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