





import java.util.List;
import java.util.ArrayList;

public class partitioning_analysis_Actor  {






    private analysis_partitioning_ComCostPartition analysis_partitioning_comcostpartition;




    private analysis_partitioning_WorkloadBalancePartition analysis_partitioning_workloadbalancepartition;




    private analysis_partitioning_BalancedPipelinePartition analysis_partitioning_balancedpipelinepartition;


    public partitioning_analysis_Actor(
    ) {
    }



    public analysis_partitioning_ComCostPartition getAnalysis_partitioning_comcostpartition() {
        return analysis_partitioning_comcostpartition;
    }

    public void setAnalysis_partitioning_comcostpartition(analysis_partitioning_ComCostPartition analysis_partitioning_comcostpartition) {
        this.analysis_partitioning_comcostpartition = analysis_partitioning_comcostpartition;
    }
    public analysis_partitioning_WorkloadBalancePartition getAnalysis_partitioning_workloadbalancepartition() {
        return analysis_partitioning_workloadbalancepartition;
    }

    public void setAnalysis_partitioning_workloadbalancepartition(analysis_partitioning_WorkloadBalancePartition analysis_partitioning_workloadbalancepartition) {
        this.analysis_partitioning_workloadbalancepartition = analysis_partitioning_workloadbalancepartition;
    }
    public analysis_partitioning_BalancedPipelinePartition getAnalysis_partitioning_balancedpipelinepartition() {
        return analysis_partitioning_balancedpipelinepartition;
    }

    public void setAnalysis_partitioning_balancedpipelinepartition(analysis_partitioning_BalancedPipelinePartition analysis_partitioning_balancedpipelinepartition) {
        this.analysis_partitioning_balancedpipelinepartition = analysis_partitioning_balancedpipelinepartition;
    }

}