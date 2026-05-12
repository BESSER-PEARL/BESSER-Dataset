





import java.util.List;
import java.util.ArrayList;

public class Ranking  {

    private boolean multians;
    private String c1__c2__c3__c4;
    private String answer;
    private String question;



    public Ranking(
        boolean multians,        String c1__c2__c3__c4,        String answer,        String question    ) {
        this.multians = multians;
        this.c1__c2__c3__c4 = c1__c2__c3__c4;
        this.answer = answer;
        this.question = question;
    }


    public boolean getMultians() {
        return multians;
    }

    public void setMultians(boolean multians) {
        this.multians = multians;
    }
    public String getC1__c2__c3__c4() {
        return c1__c2__c3__c4;
    }

    public void setC1__c2__c3__c4(String c1__c2__c3__c4) {
        this.c1__c2__c3__c4 = c1__c2__c3__c4;
    }
    public String getAnswer() {
        return answer;
    }

    public void setAnswer(String answer) {
        this.answer = answer;
    }
    public String getQuestion() {
        return question;
    }

    public void setQuestion(String question) {
        this.question = question;
    }


}