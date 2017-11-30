# Title: Monte Carlo Simulation on Airport Security Check

## Team Member(s): Sixuan Shen, Mengfei Liang

## Monte Carlo Simulation Scenario & Purpose:
Scenario：In our project, we simulate the airport security check. According to the real life situation, the wait time in the security check is decided by various variables. As we all know, the volume of passengers obviously increase on big holidays, like the Thanksgiving break or Christmas. Meanwhile, even on the normal week, the wait time of the security check may differ between weekdays and weekends. This project plan to simulate the security check on weekdays (not in holidays) scenario, on weekends(not in holidays) scenario, on holiday weekdays scenario and on holiday weekend scenario. This subdivision scenario could better simulate the real-life airport security check.

Purpose：With the rapid development of transportation, more and more people tend to choose airplane as their travel tool. But before getting on the plane, the passengers are supposed to pass the airport check and the time of airport check is unsure. This Monte Carlo simulation on airport security  check simulates scenarios in different time period, which can provide passengers a estimated wait time in the checkpoint. Not only on the normal days, but also on special holidays, people are able to know when they need to arrive at the security checkpoint in advance so that they can catch on their plane in time.

The data this project used to simulate the real-life situation is from Whatsbusy website. And we choose Chicago Ohare Airport to simulate by setting the terminal(international or domestic) variable, date variable, etc.

## Hypothesis before running the simulation:

* International terminal: 1
* Domestic terminal: 3
* Check-in counter in each terminal: 5

Assumptions:
* Each passengers passing the security check is independent and identity distributed.
* The security check counter treat passengers at same speed. (* If time permits, we would add a additional exception situation: if people is regarded as carrying prohibited items, the check counter which deal with this situation will temporarily close.)
* Each passenger’s average passing time in international terminal is 1 time more than in domestic terminal since international passengers usually carry more luggages and the restriction on them is more strict.
* The security checkpoint can treat 180 passengers at an hour.

Hypothesis:

* On weekdays in normal week, passenger’s average passing time for security check is 0-10min.
* On weekends, passenger’s average passing time will increase by 5-10min than in normal week.
* In holidays,  passenger’s average passing time would double when compared with time on same day in normal week.
* Passenger’s average passing time spent on international terminal would double when compared with time
on domestic terminal on the same day.

## Simulation's variables of uncertainty
* date_time:The number of passengers come to the airport during a certain date and time. The date is used to determine whether 
  today is in weekday or in weekend. And whether it is around the holiday(from two days before the holiday and two days after   the holiday). There are four time ranges in one day, 6am-12pm, 12pm-6pm,6pm-12am,12am-6am.
* domterminal1,domterminal2,domterminal3,intterminal: Which terminal(international or domestic) each passenger goes to. Each     passenger would be assigned to one airport terminal randomly.
* checkin_time: The check-in time for each passenger. This variable is also random for each passenger, the number would be       between 1s to 120s. 
* extra_checktime: Additional check-in time for those passengers bring liquid, and other things that cannot be taken on board.
  The system would pick up those passengers need extra check-in time randomly, the probability would between 1/500 and 1/10.
  
## Instructions on how to use the program:
    After running this program, users would need to input their date and time period of when they would arrive the airport. And the output of the program is the average wait time for passengers in the security checkpoint in this period.
    With the output from the simulation, it's able to compare it with the former hypothesis. Is the average wait time of check-in would be between 10 and 15 minutes? Is the average wait time during the weekend would be greater than the average wait time during the weekdays? 
    Our program aims to be a useful tuturiol for passengers, they can easily check how long they should arrive in advance to pass the airport security check in time.

## Sources Used:
Reference Data：http://www.whatsbusy.com/airport/MCO/20171129T020000 

Monte Carlo Simulation：https://en.wikipedia.org/wiki/Monte_Carlo_method                               https://courses.ischool.illinois.edu/pluginfile.php/335371/mod_resource/content/1/MillerRanum%203.4%20Queues%20%20Simulations.pdf
