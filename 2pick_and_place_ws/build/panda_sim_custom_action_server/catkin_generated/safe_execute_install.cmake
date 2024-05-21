execute_process(COMMAND "/home/ubuntu20-04/ros1_workspaces/2pick_and_place_ws/build/panda_sim_custom_action_server/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/ubuntu20-04/ros1_workspaces/2pick_and_place_ws/build/panda_sim_custom_action_server/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
