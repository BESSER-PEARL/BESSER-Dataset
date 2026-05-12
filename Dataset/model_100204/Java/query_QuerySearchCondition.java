





import java.util.List;
import java.util.ArrayList;

public class query_QuerySearchCondition extends expressions_SearchCondition, SQLQueryObject {

    private boolean negatedCondition;





    private query_MergeOnCondition query_mergeoncondition;




    private query_QueryDeleteStatement query_querydeletestatement;




    private query_QueryDeleteStatement query_querydeletestatement;




    private query_ValueExpressionCaseSearchContent query_valueexpressioncasesearchcontent;




    private query_QueryUpdateStatement query_queryupdatestatement;




    private query_MergeOnCondition query_mergeoncondition;




    private query_QueryUpdateStatement query_queryupdatestatement;




    private query_ValueExpressionCaseSearchContent query_valueexpressioncasesearchcontent;


    public query_QuerySearchCondition(
        boolean negatedCondition    ) {
        super(
        );
        this.negatedCondition = negatedCondition;
    }


    public boolean getNegatedcondition() {
        return negatedCondition;
    }

    public void setNegatedcondition(boolean negatedCondition) {
        this.negatedCondition = negatedCondition;
    }

    public query_MergeOnCondition getQuery_mergeoncondition() {
        return query_mergeoncondition;
    }

    public void setQuery_mergeoncondition(query_MergeOnCondition query_mergeoncondition) {
        this.query_mergeoncondition = query_mergeoncondition;
    }
    public query_QueryDeleteStatement getQuery_querydeletestatement() {
        return query_querydeletestatement;
    }

    public void setQuery_querydeletestatement(query_QueryDeleteStatement query_querydeletestatement) {
        this.query_querydeletestatement = query_querydeletestatement;
    }
    public query_QueryDeleteStatement getQuery_querydeletestatement() {
        return query_querydeletestatement;
    }

    public void setQuery_querydeletestatement(query_QueryDeleteStatement query_querydeletestatement) {
        this.query_querydeletestatement = query_querydeletestatement;
    }
    public query_ValueExpressionCaseSearchContent getQuery_valueexpressioncasesearchcontent() {
        return query_valueexpressioncasesearchcontent;
    }

    public void setQuery_valueexpressioncasesearchcontent(query_ValueExpressionCaseSearchContent query_valueexpressioncasesearchcontent) {
        this.query_valueexpressioncasesearchcontent = query_valueexpressioncasesearchcontent;
    }
    public query_QueryUpdateStatement getQuery_queryupdatestatement() {
        return query_queryupdatestatement;
    }

    public void setQuery_queryupdatestatement(query_QueryUpdateStatement query_queryupdatestatement) {
        this.query_queryupdatestatement = query_queryupdatestatement;
    }
    public query_MergeOnCondition getQuery_mergeoncondition() {
        return query_mergeoncondition;
    }

    public void setQuery_mergeoncondition(query_MergeOnCondition query_mergeoncondition) {
        this.query_mergeoncondition = query_mergeoncondition;
    }
    public query_QueryUpdateStatement getQuery_queryupdatestatement() {
        return query_queryupdatestatement;
    }

    public void setQuery_queryupdatestatement(query_QueryUpdateStatement query_queryupdatestatement) {
        this.query_queryupdatestatement = query_queryupdatestatement;
    }
    public query_ValueExpressionCaseSearchContent getQuery_valueexpressioncasesearchcontent() {
        return query_valueexpressioncasesearchcontent;
    }

    public void setQuery_valueexpressioncasesearchcontent(query_ValueExpressionCaseSearchContent query_valueexpressioncasesearchcontent) {
        this.query_valueexpressioncasesearchcontent = query_valueexpressioncasesearchcontent;
    }

}