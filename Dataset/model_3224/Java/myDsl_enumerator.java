





import java.util.List;
import java.util.ArrayList;

public class myDsl_enumerator  {






    private myDsl_constant_expression mydsl_constant_expression;




    private myDsl_EnumeratorListLinhaAction mydsl_enumeratorlistlinhaaction;




    private myDsl_enumerator_list mydsl_enumerator_list;


    public myDsl_enumerator(
    ) {
    }



    public myDsl_constant_expression getMydsl_constant_expression() {
        return mydsl_constant_expression;
    }

    public void setMydsl_constant_expression(myDsl_constant_expression mydsl_constant_expression) {
        this.mydsl_constant_expression = mydsl_constant_expression;
    }
    public myDsl_EnumeratorListLinhaAction getMydsl_enumeratorlistlinhaaction() {
        return mydsl_enumeratorlistlinhaaction;
    }

    public void setMydsl_enumeratorlistlinhaaction(myDsl_EnumeratorListLinhaAction mydsl_enumeratorlistlinhaaction) {
        this.mydsl_enumeratorlistlinhaaction = mydsl_enumeratorlistlinhaaction;
    }
    public myDsl_enumerator_list getMydsl_enumerator_list() {
        return mydsl_enumerator_list;
    }

    public void setMydsl_enumerator_list(myDsl_enumerator_list mydsl_enumerator_list) {
        this.mydsl_enumerator_list = mydsl_enumerator_list;
    }

}