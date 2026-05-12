





import java.util.List;
import java.util.ArrayList;

public class Essay  {

    private String answer;
    private boolean multians;
    private String question;
    private String c1__c2__c3__c4;



    public Essay(
        String answer,        boolean multians,        String question,        String c1__c2__c3__c4    ) {
        this.answer = answer;
        this.multians = multians;
        this.question = question;
        this.c1__c2__c3__c4 = c1__c2__c3__c4;
    }


    public String getAnswer() {
        return answer;
    }

    public void setAnswer(String answer) {
        this.answer = answer;
    }
    public boolean getMultians() {
        return multians;
    }

    public void setMultians(boolean multians) {
        this.multians = multians;
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


}