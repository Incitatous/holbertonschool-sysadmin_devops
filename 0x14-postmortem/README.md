#Postmortem

##Summary
On Friday, 31 March, 2017, Pied Piper experienced a temporary outage after switching to in-house servers that were not able to handle the amount of traffic our company encounters on a daily basis.

##Affected Services
All Pied Piper services were affected: our compression platform would not function and even our main website went down.

##Impact 
Fortunately, we were still in the beta phase and as such, no “customers” were impacted. However, had the outage not been dealt with as promptly, it could have definitely impacted our public image and endangered our growth.

##Outage Duration
Between the switch to our own servers to the rollback to our former servers, the outage lasted for six hours.

##Cause
The primary cause of the outage was the way we underestimated the amount of traffic we would be receiving and our subsequent decision to switch to our own servers, which were not properly configured to handle that much traffic. The secondary cause, was our decision that the servers we were primarily using were not best adapted to our purposes. It ended being a false assertion that could have tarnished our reputation on the medium to long term.

##Resolution
We decided to resolve the issue by rolling back to the previous servers. That was not an easy to made decision as we had spent many hours setting our DNS with what we thought would be enough web balancers. We had to decide whether to fix our own servers – which would have taken at least several hours, if not days – or to rollback to the former servers we used previously and be back to square one. We finally decided on the latter which solved our issue.

##Timeline of events
At 14:50 Pacific Time on March 31st, after running a series of tests for a week, we decided that our in-house servers were enough to handle our traffic and that they weren’t hampering the speed of our service. We thus decided to implement the change. The rollout went fine or so it seems for the first ten minutes. However, we rapidly realized we had greatly underestimated the amount of traffic that our beta was going to attract. At 15:20, none of our load balancers were functioning anymore. We contacted the vendor who was previously providing our servers, and their reaction was quick enough so that our platform was up again a few hours later.

##Problems with our response
We didn’t encounter any specific issue during our response as we basically decided to roll back to our previous architecture. Also, our vendor was of the best assistance and definitely met our needs in terms of reactivity.

##Preventative measures to take
In the future, we will especially make sure that our servers can support much more traffic than we expect and spend more time testing before implementing a new architecture.

##Detection Method
We detected this issue quickly as we constantly monitor the state of our servers.

##Changes to make in future outage responses 
In the future, we will focus on the aforementioned preventative measures to ensure our beta testers get the quality of service they deserve.
