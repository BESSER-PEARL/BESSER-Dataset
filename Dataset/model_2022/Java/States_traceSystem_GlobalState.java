





import java.util.List;
import java.util.ArrayList;

public class States_traceSystem_GlobalState  {






    private traceSystem_States_Activity_trace_State tracesystem_states_activity_trace_state;




    private traceSystem_States_ActivityNode_running_State tracesystem_states_activitynode_running_state;




    private traceSystem_States_InputValue_value_State tracesystem_states_inputvalue_value_state;




    private traceSystem_States_Variable_currentValue_State tracesystem_states_variable_currentvalue_state;




    private traceSystem_States_InputValue_variable_State tracesystem_states_inputvalue_variable_state;




    private traceSystem_States_ForkedToken_baseToken_State tracesystem_states_forkedtoken_basetoken_state;




    private traceSystem_States_Token_holder_State tracesystem_states_token_holder_state;




    private traceSystem_States_ActivityEdge_offers_State tracesystem_states_activityedge_offers_state;




    private traceSystem_States_Offer_offeredTokens_State tracesystem_states_offer_offeredtokens_state;




    private traceSystem_States_Input_inputValues_State tracesystem_states_input_inputvalues_state;




    private traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State tracesystem_states_forkedtoken_basetokeniswithdrawn_state;




    private traceSystem_States_ForkedToken_remainingOffersCount_State tracesystem_states_forkedtoken_remainingofferscount_state;




    private traceSystem_States_ActivityNode_heldTokens_State tracesystem_states_activitynode_heldtokens_state;




    private traceSystem_States_Trace_executedNodes_State tracesystem_states_trace_executednodes_state;


    public States_traceSystem_GlobalState(
    ) {
    }



    public traceSystem_States_Activity_trace_State getTracesystem_states_activity_trace_state() {
        return tracesystem_states_activity_trace_state;
    }

    public void setTracesystem_states_activity_trace_state(traceSystem_States_Activity_trace_State tracesystem_states_activity_trace_state) {
        this.tracesystem_states_activity_trace_state = tracesystem_states_activity_trace_state;
    }
    public traceSystem_States_ActivityNode_running_State getTracesystem_states_activitynode_running_state() {
        return tracesystem_states_activitynode_running_state;
    }

    public void setTracesystem_states_activitynode_running_state(traceSystem_States_ActivityNode_running_State tracesystem_states_activitynode_running_state) {
        this.tracesystem_states_activitynode_running_state = tracesystem_states_activitynode_running_state;
    }
    public traceSystem_States_InputValue_value_State getTracesystem_states_inputvalue_value_state() {
        return tracesystem_states_inputvalue_value_state;
    }

    public void setTracesystem_states_inputvalue_value_state(traceSystem_States_InputValue_value_State tracesystem_states_inputvalue_value_state) {
        this.tracesystem_states_inputvalue_value_state = tracesystem_states_inputvalue_value_state;
    }
    public traceSystem_States_Variable_currentValue_State getTracesystem_states_variable_currentvalue_state() {
        return tracesystem_states_variable_currentvalue_state;
    }

    public void setTracesystem_states_variable_currentvalue_state(traceSystem_States_Variable_currentValue_State tracesystem_states_variable_currentvalue_state) {
        this.tracesystem_states_variable_currentvalue_state = tracesystem_states_variable_currentvalue_state;
    }
    public traceSystem_States_InputValue_variable_State getTracesystem_states_inputvalue_variable_state() {
        return tracesystem_states_inputvalue_variable_state;
    }

    public void setTracesystem_states_inputvalue_variable_state(traceSystem_States_InputValue_variable_State tracesystem_states_inputvalue_variable_state) {
        this.tracesystem_states_inputvalue_variable_state = tracesystem_states_inputvalue_variable_state;
    }
    public traceSystem_States_ForkedToken_baseToken_State getTracesystem_states_forkedtoken_basetoken_state() {
        return tracesystem_states_forkedtoken_basetoken_state;
    }

    public void setTracesystem_states_forkedtoken_basetoken_state(traceSystem_States_ForkedToken_baseToken_State tracesystem_states_forkedtoken_basetoken_state) {
        this.tracesystem_states_forkedtoken_basetoken_state = tracesystem_states_forkedtoken_basetoken_state;
    }
    public traceSystem_States_Token_holder_State getTracesystem_states_token_holder_state() {
        return tracesystem_states_token_holder_state;
    }

    public void setTracesystem_states_token_holder_state(traceSystem_States_Token_holder_State tracesystem_states_token_holder_state) {
        this.tracesystem_states_token_holder_state = tracesystem_states_token_holder_state;
    }
    public traceSystem_States_ActivityEdge_offers_State getTracesystem_states_activityedge_offers_state() {
        return tracesystem_states_activityedge_offers_state;
    }

    public void setTracesystem_states_activityedge_offers_state(traceSystem_States_ActivityEdge_offers_State tracesystem_states_activityedge_offers_state) {
        this.tracesystem_states_activityedge_offers_state = tracesystem_states_activityedge_offers_state;
    }
    public traceSystem_States_Offer_offeredTokens_State getTracesystem_states_offer_offeredtokens_state() {
        return tracesystem_states_offer_offeredtokens_state;
    }

    public void setTracesystem_states_offer_offeredtokens_state(traceSystem_States_Offer_offeredTokens_State tracesystem_states_offer_offeredtokens_state) {
        this.tracesystem_states_offer_offeredtokens_state = tracesystem_states_offer_offeredtokens_state;
    }
    public traceSystem_States_Input_inputValues_State getTracesystem_states_input_inputvalues_state() {
        return tracesystem_states_input_inputvalues_state;
    }

    public void setTracesystem_states_input_inputvalues_state(traceSystem_States_Input_inputValues_State tracesystem_states_input_inputvalues_state) {
        this.tracesystem_states_input_inputvalues_state = tracesystem_states_input_inputvalues_state;
    }
    public traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State getTracesystem_states_forkedtoken_basetokeniswithdrawn_state() {
        return tracesystem_states_forkedtoken_basetokeniswithdrawn_state;
    }

    public void setTracesystem_states_forkedtoken_basetokeniswithdrawn_state(traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State tracesystem_states_forkedtoken_basetokeniswithdrawn_state) {
        this.tracesystem_states_forkedtoken_basetokeniswithdrawn_state = tracesystem_states_forkedtoken_basetokeniswithdrawn_state;
    }
    public traceSystem_States_ForkedToken_remainingOffersCount_State getTracesystem_states_forkedtoken_remainingofferscount_state() {
        return tracesystem_states_forkedtoken_remainingofferscount_state;
    }

    public void setTracesystem_states_forkedtoken_remainingofferscount_state(traceSystem_States_ForkedToken_remainingOffersCount_State tracesystem_states_forkedtoken_remainingofferscount_state) {
        this.tracesystem_states_forkedtoken_remainingofferscount_state = tracesystem_states_forkedtoken_remainingofferscount_state;
    }
    public traceSystem_States_ActivityNode_heldTokens_State getTracesystem_states_activitynode_heldtokens_state() {
        return tracesystem_states_activitynode_heldtokens_state;
    }

    public void setTracesystem_states_activitynode_heldtokens_state(traceSystem_States_ActivityNode_heldTokens_State tracesystem_states_activitynode_heldtokens_state) {
        this.tracesystem_states_activitynode_heldtokens_state = tracesystem_states_activitynode_heldtokens_state;
    }
    public traceSystem_States_Trace_executedNodes_State getTracesystem_states_trace_executednodes_state() {
        return tracesystem_states_trace_executednodes_state;
    }

    public void setTracesystem_states_trace_executednodes_state(traceSystem_States_Trace_executedNodes_State tracesystem_states_trace_executednodes_state) {
        this.tracesystem_states_trace_executednodes_state = tracesystem_states_trace_executednodes_state;
    }

}